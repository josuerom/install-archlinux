# Modificado por Josué Romero
# Creado por Antonio Sarosi
# https://twitter.com/josueromr
# https://github.com/josuerom/install-archlinux

from libqtile.config import Key
from libqtile.command import lazy

win = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [

    # ------------ Window Configs ------------
    # Posicionate en otra ventana
    ([win], "j", lazy.layout.down()),
    ([win], "k", lazy.layout.up()),
    ([win], "h", lazy.layout.left()),
    ([win], "l", lazy.layout.right()),

    # Redimenziona las ventanas
    ([win, "shift"], "l", lazy.layout.grow()),
    ([win, "shift"], "h", lazy.layout.shrink()),

    # Trabaja con la ventana flotante
    ([win, "shift"], "f", lazy.window.toggle_floating()),

    # Mueva la venta actual a otra parte de la pantalla
    ([win, "shift"], "j", lazy.layout.shuffle_down()),
    ([win, "shift"], "k", lazy.layout.shuffle_up()),

    # Cambia la distribución de las ventanas en el área de trabajo
    ([win], "Tab", lazy.next_layout()),
    ([win, "shift"], "Tab", lazy.prev_layout()),

    # Cerrar ventana abierta
    ([win], "w", lazy.window.kill()),

    # Cambia el enfoque de los monitores
    ([win], "period", lazy.next_screen()),
    ([win], "comma", lazy.prev_screen()),

    # Reiniciar qtile
    ([win, "control"], "r", lazy.restart()),

    # Cerrar sesión
    ([win, "control"], "q", lazy.shutdown()),
    ([win], "r", lazy.spawncmd()),

    # ------------ App Configs ------------
    # Menu para lanzar programas
    ([win], "r", lazy.spawn("ulauncher")),

    # Ejecute el navegador
    ([win], "b", lazy.spawn("google-chrome-stable")),

    # Abra el explorador de archivos
    ([win], "e", lazy.spawn("nautilus")),

    # Abra la terminal
    ([win], "Return", lazy.spawn("alacritty")),

    # Enciende el modo nocturno
    ([win], "m", lazy.spawn("redshift -O 2400")),
    ([win, "shift"], "m", lazy.spawn("redshift -x")),

    # Captura de pantalla automatica y manual
    ([win], "s", lazy.spawn("scrot")),
    ([win, "shift"], "s", lazy.spawn("scrot -s")),
     
    # Otros lanzamientos de programas
    ([win], "c", lazy.spawn("code")),
    ([win], "v", lazy.spawn("vlc")),
    ([win], "i", lazy.spawn("idea")),
    ([win], "c", lazy.spawn("gnome-calculator")),
    ([win], "t", lazy.spawn("teams")),
    ([win], "i", lazy.spawn("gnome-control-center")),
    (["control", "shift"], "Esc", lazy.spawn("gnome-system-monitor")),
    #([win], "p", lazy.spawn("gnome-system-monitor")),
    #([win], "", lazy.spawn("")),
    #([win], "", lazy.spawn("")),
    
    # ------------ Configuración de Hardware ------------
    # Volumen
    ([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")),
    ([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")),
    ([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
]]