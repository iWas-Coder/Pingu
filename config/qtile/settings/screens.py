# Pingu's Qtile Settings (screens) Config File
# (c) iWas. All rights reserved.
# https://github.com/iWas-Coder/Pingu

from libqtile.config import Screen
from .widgets import screen_bar, primary_widgets, secondary_widgets


# === Screens === #
screens = [
    Screen(top = screen_bar(primary_widgets)),
    Screen(top = screen_bar(secondary_widgets))
]
