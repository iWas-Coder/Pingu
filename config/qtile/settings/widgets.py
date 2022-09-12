# Pingu's Qtile Settings (widgets) Config File
# (c) iWas. All rights reserved.
# https://github.com/iWas-Coder/Pingu

from os import path
from libqtile import widget
from libqtile import bar
from .path import qtile_path


# === Default values === #
widget_defaults = {
    "font": "JetBrainsMono Nerd Font",
    "fontsize": 11,
    "padding": 3
}
extension_defaults = widget_defaults.copy()


# === Create Bar function === #
screen_bar = lambda widgets: bar.Bar(widgets, 29, opacity = 0.65)

# === Primary Screen Widgets === #
primary_widgets = [
    # Groups & window title (left section)
    widget.GroupBox(
        foreground=["#282ab5", "#282ab5"],
        background=["#0f101a", "#0f101a"],
        font='JetBrainsMono Nerd Font',
        fontsize=19,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=["#f1ffff", "#f1ffff"],
        inactive=["#4c566a", "#4c566a"],
        rounded=False,
        highlight_method='block',
        urgent_alert_method='block',
        urgent_border=["#F07178", "#F07178"],
        this_current_screen_border=["#a151d3", "#a151d3"],
        this_screen_border=["#353c4a", "#353c4a"],
        other_current_screen_border=["#0f101a", "#0f101a"],
        other_screen_border=["#0f101a", "#0f101a"],
        disable_drag=True
    ),
    widget.WindowName(
        foreground=["#a151d3", "#a151d3"],
        background=["#0f101a", "#0f101a"],
        fontsize=10,
        padding=10
    ),
    # First separator (black -> yellow)
    widget.Image(filename = path.join(qtile_path, "settings", "assets", "bar1.png")),
    # Updates (yellow section)
    widget.TextBox(
        background=["#ffd47e", "#ffd47e"],
        foreground=["#0f101a", "#0f101a"],
        text=' '
    ),
    widget.CheckUpdates(
        background=["#ffd47e", "#ffd47e"],
        foreground=["#0f101a", "#0f101a"],
        colour_have_updates=["#0f101a", "#0f101a"],
        colour_no_updates=["#0f101a", "#0f101a"],
        no_update_string='0',
        display_format='{updates}',
        update_interval=300,
        custom_command='checkupdates',
    ),
    # Second separator (yellow -> orange)
    widget.Image(filename = path.join(qtile_path, "settings", "assets", "bar2.png")),
    # Network (orange section)
    widget.TextBox(
        foreground=["#0f101a", "#0f101a"],
        background=["#fb9f7f", "#fb9f7f"],
        text='  '
    ),
    widget.Net(
        foreground=["#0f101a", "#0f101a"],
        background=["#fb9f7f", "#fb9f7f"], 
        interface='ens33'
    ),
    # Third separator (orange -> red)
    widget.Image(filename = path.join(qtile_path, "settings", "assets", "bar3.png")),
    # Layout (red section)
    widget.CurrentLayoutIcon(
        foreground=["#0f101a", "#0f101a"],
        background=["#F07178", "#F07178"],
        scale=0.65
    ),
    widget.CurrentLayout(
        foreground=["#0f101a", "#0f101a"],
        background=["#F07178", "#F07178"]
    ),
    # Fourth separator (red -> purple)
    widget.Image(filename = path.join(qtile_path, "settings", "assets", "bar4.png")),
    # Clock (purple section)
    widget.TextBox(
        background=["#a151d3", "#a151d3"],
        foreground=["#0f101a", "#0f101a"],
        text='  '
    ),
    widget.Clock(
        background=["#a151d3", "#a151d3"],
        foreground=["#0f101a", "#0f101a"],
        format='%d/%m/%Y - %H:%M '
    ),
    # Last separator (purple -> black)
    widget.Image(filename = path.join(qtile_path, "settings", "assets", "bar5.png")),
    widget.Systray()
]

# === Secondary Screen Widgets === #
secondary_widgets = [
    # Groups & window title (left section)
    widget.GroupBox(
        foreground=["#282ab5", "#282ab5"],
        background=["#0f101a", "#0f101a"],
        font='JetBrainsMono Nerd Font',
        fontsize=19,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=["#f1ffff", "#f1ffff"],
        inactive=["#4c566a", "#4c566a"],
        rounded=False,
        highlight_method='block',
        urgent_alert_method='block',
        urgent_border=["#F07178", "#F07178"],
        this_current_screen_border=["#a151d3", "#a151d3"],
        this_screen_border=["#353c4a", "#353c4a"],
        other_current_screen_border=["#0f101a", "#0f101a"],
        other_screen_border=["#0f101a", "#0f101a"],
        disable_drag=True
    ),
    widget.WindowName(
        foreground=["#a151d3", "#a151d3"],
        background=["#0f101a", "#0f101a"],
        fontsize=10,
        padding=10
    ),
    # First separator (black -> yellow)
    widget.Image(filename = path.join(qtile_path, "settings", "assets", "bar1.png")),
    # Updates (yellow section)
    widget.TextBox(
        background=["#ffd47e", "#ffd47e"],
        foreground=["#0f101a", "#0f101a"],
        text=' '
    ),
    widget.CheckUpdates(
        background=["#ffd47e", "#ffd47e"],
        foreground=["#0f101a", "#0f101a"],
        colour_have_updates=["#0f101a", "#0f101a"],
        colour_no_updates=["#0f101a", "#0f101a"],
        no_update_string='0',
        display_format='{updates}',
        update_interval=300,
        custom_command='checkupdates',
    ),
    # Second separator (yellow -> orange)
    widget.Image(filename = path.join(qtile_path, "settings", "assets", "bar2.png")),
    # COMPACTED Network (orange section)
    widget.TextBox(
        foreground=["#0f101a", "#0f101a"],
        background=["#fb9f7f", "#fb9f7f"],
        text='  '
    ),
    # Third separator (orange -> red)
    widget.Image(filename = path.join(qtile_path, "settings", "assets", "bar3.png")),
    # Layout (red section)
    widget.CurrentLayoutIcon(
        foreground=["#0f101a", "#0f101a"],
        background=["#F07178", "#F07178"],
        scale=0.65
    ),
    widget.CurrentLayout(
        foreground=["#0f101a", "#0f101a"],
        background=["#F07178", "#F07178"]
    ),
    # Fourth separator (red -> purple)
    widget.Image(filename = path.join(qtile_path, "settings", "assets", "bar4.png")),
    # Clock (purple section)
    widget.TextBox(
        background=["#a151d3", "#a151d3"],
        foreground=["#0f101a", "#0f101a"],
        text='  '
    ),
    widget.Clock(
        background=["#a151d3", "#a151d3"],
        foreground=["#0f101a", "#0f101a"],
        format='%d/%m/%Y - %H:%M '
    ),
    # Last separator (purple -> black)
    widget.Image(filename = path.join(qtile_path, "settings", "assets", "bar5.png")),
    widget.Systray()
]
