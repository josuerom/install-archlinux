# Modificado por Josué Romero
# Creado por Antonio Sarosi
# https://twitter.com/josueromr
# https://github.com/josuerom/arch-linux

from libqtile.config import Key
from libqtile.command import lazy

win = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [

    # ------------ Window Configs ------------
    # Switch between windows in current stack pane
    ([win], "j", lazy.layout.down()),
    ([win], "k", lazy.layout.up()),
    ([win], "h", lazy.layout.left()),
    ([win], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([win, "shift"], "l", lazy.layout.grow()),
    ([win, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([win, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([win, "shift"], "j", lazy.layout.shuffle_down()),
    ([win, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([win], "Tab", lazy.next_layout()),
    ([win, "shift"], "Tab", lazy.prev_layout()),

    # Mata las ventanas
    ([win], "w", lazy.window.kill()),

    # Cambia el enfoque de los monitores
    ([win], "period", lazy.next_screen()),
    ([win], "comma", lazy.prev_screen()),

    # Reiniciar Qtile
    ([win, "control"], "r", lazy.restart()),
    # Cerrar sesión
    ([win, "control"], "q", lazy.shutdown()),
    ([win], "r", lazy.spawncmd()),

    # ------------ App Configs ------------
    # Menu para lanzar programas
    ([win], "m", lazy.spawn("rofi -show drun")),

    # Ventana de navegación
    ([win, "shift"], "m", lazy.spawn("rofi -show")),

    # Navegador
    #([win], "b", lazy.spawn("firefox")),
    ([win], "b", lazy.spawn("google-chrome-stable")),

    # Explorador de archivos
    ([win], "e", lazy.spawn("thunar")),

    # Terminal
    ([win], "Return", lazy.spawn("alacritty")),

    # Modo cuida ojos
    ([win], "r", lazy.spawn("redshift -O 2400")),
    ([win, "shift"], "r", lazy.spawn("redshift -x")),

    # Captura de pantalla
    ([win], "s", lazy.spawn("scrot")),
    ([win, "shift"], "s", lazy.spawn("scrot -s")),
     
    # Others commands
    ([win], "c", lazy.spawn("code")),
    #([win], "", lazy.spawn("")),
    #([win], "", lazy.spawn("")),
    #([win], "", lazy.spawn("")),
    #([win], "", lazy.spawn("")),
    
    # ------------ Hardware Configs ------------
    # Volumen
    ([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")),
    ([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")),
    ([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Brillo
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +20%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 20%-")),
]]
