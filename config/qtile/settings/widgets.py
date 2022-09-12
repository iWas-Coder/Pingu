# Pingu's Qtile Settings (widgets) Config File
# (c) iWas. All rights reserved.
# https://github.com/iWas-Coder/Pingu

from libqtile import widget
from libqtile import bar


# === Default values === #
widget_defaults = {
    "font": "JetBrainsMono Nerd Font",
    "fontsize": 11,
    "padding": 3
}
extension_defaults = widget_defaults.copy()

# === Create Bar function === #
screen_bar = lambda widgets: bar.Bar(widgets, 29, opacity = 0.65)

# === Widgets === #
primary_widgets = [
    # Groups & window title (left section)
    widget.GroupBox(),
    widget.WindowName(),
    # First separator (black -> yellow)
    widget.Image(),
    # Updates (yellow section)
    widget.TextBox(),
    widget.CheckUpdates(),
    # Second separator (yellow -> orange)
    widget.Image(),
    # Network (orange section)
    widget.TextBox(),
    widget.Net(),
    # Third separator (orange -> red)
    widget.Image(),
    # Layout (red section)
    widget.CurrentLayoutIcon(),
    widget.CurrentLayout(),
    # Fourth separator (red -> purple)
    widget.Image(),
    # Clock (purple section)
    widget.TextBox(),
    widget.Clock(),
    # Last separator (purple -> black)
    widget.Image(),
    widget.Systray()
]
secondary_widgets = [
    # Groups & window title (left section)
    widget.GroupBox(),
    widget.WindowName(),
    # First separator (black -> yellow)
    widget.Image(),
    # Updates (yellow section)
    widget.TextBox(),
    widget.CheckUpdates(),
    # Second separator (yellow -> orange)
    widget.Image(),
    # COMPACTED Network (orange section)
    widget.TextBox(),
    # Third separator (orange -> red)
    widget.Image(),
    # Layout (red section)
    widget.CurrentLayoutIcon(),
    widget.CurrentLayout(),
    # Fourth separator (red -> purple)
    widget.Image(),
    # Clock (purple section)
    widget.TextBox(),
    widget.Clock(),
    # Last separator (purple -> black)
    widget.Image(),
    widget.Systray()
]
