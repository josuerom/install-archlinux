# Modificado por Josué Romero
# Creado por Antonio Sarosi
# https://twitter.com/josueromr
# https://github.com/josuerom/install-archlinux

from libqtile.config import Key
from libqtile.command import lazy

# declaro las teclas líderes
win = "mod4"
ctrl = "control"
shift = "shift"
tab = "Tab"
punto = "period"
coma = "comma"

keys = [Key(key[0], key[1], *key[2:]) for key in [

    # ------------ Ajustes para el Gestor de Ventanas ------------
    # Posicionate en otra ventana
    ([win], "j", lazy.layout.down()),
    ([win], "k", lazy.layout.up()),
    ([win], "h", lazy.layout.left()),
    ([win], "l", lazy.layout.right()),
    # Redimenziona las ventanas
    ([win, shift], "l", lazy.layout.grow()),
    ([win, shift], "h", lazy.layout.shrink()),

    # Trabaja con la ventana flotante
    ([win, shift], "f", lazy.window.toggle_floating()),

    # Mueva la venta actual a otra parte de la pantalla
    ([win, shift], "j", lazy.layout.shuffle_down()),
    ([win, shift], "k", lazy.layout.shuffle_up()),

    # Cambia la distribución de las ventanas en el área de trabajo
    ([win], tab, lazy.next_layout()),
    ([win, shift], tab, lazy.prev_layout()),

    # Cerrar ventana abierta
    ([win], "w", lazy.window.kill()),

    # Cambia el enfoque de los monitores
    ([win], punto, lazy.next_screen()),
    ([win], coma, lazy.prev_screen()),

    # Reiniciar qtile
    ([win, ctrl], "r", lazy.restart()),

    # Cerrar sesión
    ([win, ctrl], "q", lazy.shutdown()),
    
    ([win], "r", lazy.spawncmd()),

    # ------------ Lanzamiento de Programas ------------
    # Menu para lanzar programas
    #([win, ctrl], "r", lazy.spawn("rofi")),
    #([ctrl], "r", lazy.spawn("ulauncher")),

    # Ejecute el navegador
    ([win], "b", lazy.spawn("google-chrome-stable")),

    # Abra el explorador de archivos
    ([win], "e", lazy.spawn("nautilus")),

    # Abra la terminal
    ([win], "Return", lazy.spawn("alacritty")),

    # Enciende el modo nocturno
    ([win], "m", lazy.spawn("redshift -O 2400")),
    ([win, shift], "m", lazy.spawn("redshift -x")),

    # Captura de pantalla automatica y manual
    ([win], "s", lazy.spawn("scrot")),
    ([win, shift], "s", lazy.spawn("scrot -s")),
     
    # Otros lanzamientos
    ([win], "c", lazy.spawn("code")),
    ([win], "i", lazy.spawn("idea")),
    ([win], "t", lazy.spawn("teams")),
    ([win, shift], "i", lazy.spawn("gnome-control-center")),
    ([win, shift], "c", lazy.spawn("gnome-calculator")),
    ([win, shift], "p", lazy.spawn("gnome-system-monitor")),
    
    # Otras Letras Disponibles (t y u o p a f g ñ x v n)
    #([win], "", lazy.spawn("")),
    #([win], "", lazy.spawn("")),
    #([win], "", lazy.spawn("")),
    
    # ------------ Configuración de Hardware ------------
    # Volumen
    ([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")),
    ([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")),
    ([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
]]