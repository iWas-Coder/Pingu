# Pingu's Qtile Main Config File
# (c) iWas. All rights reserved.
# https://github.com/iWas-Coder/Pingu

from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import screens
from settings.mouse import mouse
from settings.path import qtile_path


# === Configuration variables === #
main = None
auto_fullscreen = True
bring_front_click = False
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = []
focus_on_window_activation = "smart"
follow_mouse_focus = True
wmname = "Pingu"
