# Pingu's Qtile Settings (mouse) Config File
# (c) iWas. All rights reserved.
# https://github.com/iWas-Coder/Pingu

from libqtile.config import Drag
from libqtile.command import lazy
from .keys import mod


# === Mouse Configuration === #
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start = lazy.window.get_position()
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start = lazy.window.get_size()
    )
]
