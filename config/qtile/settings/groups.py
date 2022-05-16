# Modificado por Josué Romero
# Creado por Antonio Sarosi
# https://twitter.com/josueromr
# https://github.com/josuerom/Install-ArchLinux

from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import win, keys

# Obten más iconos aquí -> https://www.nerdfonts.com/cheat-sheet
# Iconos en uso:
# nf-linux-archlinux
# nf-fa-firefox, 
# nf-fae-python, 
# nf-oct-terminal, 
# nf-fa-code, 
# nf-oct-github, 
# nf-oct-database

groups = [Group(i) for i in [
    "   ", "   ", "   ", "   ", "   ", "   ", "   ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([win], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([win, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
