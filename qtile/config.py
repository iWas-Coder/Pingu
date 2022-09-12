# Qtile Config File
# http://www.qtile.org/

# Wasym Atieh Alonso
# https://www.youtube.com/channel/UCjU20xg8Hv3sycHRXH5Kjng/
# https://github.com/iWas-Coder/iQtile

from os import path
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(path.expanduser('~'), '.config', 'qtile', 'autostart.sh')])


################################################################################
# KEYS
################################################################################


mod = "mod4"
alt = "mod1"
terminal = "alacritty"

keys = [
    # Focus between windows.
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Up", lazy.layout.up()),

    # Swap windows within the same layout.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),

    # Change window sizes.
    Key([mod, alt], "Right", lazy.layout.shrink()),
    Key([mod, alt], "Left", lazy.layout.grow()),

    # Change monitor focus.
    Key([mod, "control"], "Left", lazy.prev_screen()), 
    Key([mod, "control"], "Right", lazy.next_screen()),

    # WM/DE controls
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),

    # App controls
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "m", lazy.spawn("rofi -show drun")),
    Key([mod, 'shift'], "m", lazy.spawn("rofi -show")),
    Key([mod], "b", lazy.spawn("firefox")),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui")),
]


################################################################################
# GROUPS
################################################################################


groups = [Group(i) for i in ["   ", "   ", "   ", "   ", "   ", "  ", "   ", "   ", "   "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])


################################################################################
# LAYOUTS
################################################################################


layout_conf = {
     'border_focus': '#a151d3',
     'border_width': 3,
     'margin': 25
}

layouts = [
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    # layout.Max(**layout_conf),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


################################################################################
# WIDGETS
################################################################################


widget_defaults = dict(
    font='JetBrainsMonoMedium Nerd Font',
    fontsize=11,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
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
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img','bar-1.png')
                ),
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
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img','bar0.png')
                ),
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
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img','bar1.png')
                ),
                widget.CurrentLayoutIcon(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#F07178", "#F07178"],
                    scale=0.65
                ),
                widget.CurrentLayout(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#F07178", "#F07178"]
                ),
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img','bar2.png')
                ),
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
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img','bar3.png')
                ),
                widget.Systray(),
            ],
            29,
            opacity=0.65
        ),
    ),
    Screen(
        top=bar.Bar(
            [
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
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img','bar-1.png')
                ),
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
                    update_interval=1800,
                    custom_command='checkupdates',
                ),
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img','bar0.png')
                ),
                widget.TextBox(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#fb9f7f", "#fb9f7f"],
                    text='  '
                ),
                # widget.Net(
                #    foreground=["#0f101a", "#0f101a"],
                #    background=["#fb9f7f", "#fb9f7f"], 
                #    interface='ens33',
                # ),
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img','bar1.png')
                ),
                widget.CurrentLayoutIcon(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#F07178", "#F07178"],
                    scale=0.65
                ),
                widget.CurrentLayout(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#F07178", "#F07178"]
                ),
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img','bar2.png')
                ),
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
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img','bar3.png')
                ),
                widget.Systray(),
            ],
            29,
            opacity=0.65
        ),
    )
]


################################################################################
# GENERAL
################################################################################


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], border_focus='#a151d3')
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wmname = "iWas's Custom WM"
