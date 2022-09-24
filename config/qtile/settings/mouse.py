# === Qtile (MOUSE) Configuration by iWas <3 === #


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
