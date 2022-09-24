# === Qtile (MAIN) Configuration by iWas <3 === #


from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layout_conf, layouts
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import screens
from settings.mouse import mouse
from settings.path import qtile_path


# === Configuration variables === #
wmname = "pingu"
auto_fullscreen = True
auto_minimize = False
reconfigure_screens = True
bring_front_click = False
cursor_warp = False
follow_mouse_focus = False
focus_on_window_activation = "smart"
dgroups_key_binder = None
dgroups_app_rules = []
