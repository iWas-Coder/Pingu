# === Qtile (SCREENS) Configuration by iWas <3 === #


from libqtile.config import Screen
from .widgets import screen_bar, primary_widgets, secondary_widgets


# === Screens === #
screens = [
    Screen(top = screen_bar(primary_widgets)),
    Screen(top = screen_bar(secondary_widgets))
]
