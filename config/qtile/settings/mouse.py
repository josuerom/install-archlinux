# Modificado por Josué Romero
# Creado po Antonio Sarosi
# https://twitter.com/josueromr
# https://github.com/josuerom/arch-linux

from libqtile.config import Drag, Click
from libqtile.command import lazy
from .keys import win

mouse = [
    Drag(
        [win],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [win],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click([win], "Button2", lazy.window.bring_to_front())
]
