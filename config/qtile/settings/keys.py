# === Qtile (KEYS) Configuration by iWas <3 === #


from libqtile.config import Key
from libqtile.command import lazy


# === Global variables === #
# Keys
mod = "mod4"
alt = "mod1"
ctrl = "control"
# Apps
terminal = "kitty"
browser = "chromium"
browser_incognito = "chromium --incognito"
apps = "rofi -show drun"
apps_opened = "rofi -show"
clipboard_history = "rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}'"
screenshot = "flameshot gui"


# === Keys === #
keys = [
    # App menu (rofi)
    Key([ctrl], "m", lazy.spawn(apps)),
    Key([ctrl, 'shift'], "m", lazy.spawn(apps_opened)),

    # Browser (chromium)
    Key([ctrl], "b", lazy.spawn(browser)),
    Key([ctrl, "shift"], "b", lazy.spawn(browser_incognito)),
    
    # Screenshot (flameshot)
    Key([mod, "shift"], "s", lazy.spawn(screenshot)),
    
    # Clipboard history (greenclip)
    Key([mod], "v", lazy.spawn(clipboard_history)),

    # New window (terminal)
    Key([ctrl], "Return", lazy.spawn(terminal)),

    # Moving between windows
    Key([ctrl], "Up", lazy.layout.up()),
    Key([ctrl], "Right", lazy.layout.right()),
    Key([ctrl], "Down", lazy.layout.down()),
    Key([ctrl], "Left", lazy.layout.left()),

    # Moving windows between each other
    Key([ctrl, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([ctrl, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([ctrl, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([ctrl, "shift"], "Left", lazy.layout.shuffle_left()),

    # Resize window
    Key([ctrl, alt], "Right", lazy.layout.shrink()),
    Key([ctrl, alt], "Left", lazy.layout.grow()),

    # Toggle floating window
    Key([mod], "f", lazy.window.toggle_floating()),

    # Moving between monitors/screens
    Key([ctrl], "Tab", lazy.next_screen()),

    # Close window
    Key([ctrl], "w", lazy.window.kill()),
]
