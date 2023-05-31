# Modificado por Josué Romero
# Creado por Antonio Sarosi
# https://twitter.com/josueromr
# https://github.com/josuerom/install-archlinux

from libqtile.config import Key
from libqtile.command import lazy

# declaro las teclas líderes
win = "mod4"
alt = "mod1"
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

    # Refrescar configuración de qtile
    ([win, ctrl], "r", lazy.restart()),

    # Cerrar sesión
    ([win, ctrl], "q", lazy.shutdown()),
    # Bloquear pantalla
    ([win], "l", lazy.spawn("qtile-cmd -o cmd -f lock")),
    # Apagar dispositivo
    ([win, alt], "l", lazy.spawn("shutdown -h now")),

    # ------------ Lanzamiento de programas ------------
    # Rofi
    #([win, ctrl], "r", lazy.spawn("rofi")),
    # Ulauncher
    ([ctrl], "r", lazy.spawn("ulauncher")),

    # Lanzar navegador
    ([win], "b", lazy.spawn("brave-bin")),
    #([win], "b", lazy.spawn("google-chrome-stable")),
    #([win], "b", lazy.spawn("google-chrome-stable")),
    
    # Lanzar explorador de archivos
    ([win], "e", lazy.spawn("dolphin")),
    #([win], "e", lazy.spawn("thunar")),
    #([win], "e", lazy.spawn("nautilus")),

    # Lanzar terminal
    ([win], "Return", lazy.spawn("alacritty")),
    #([win], "Return", lazy.spawn("kitty")),
    #([win], "Return", lazy.spawn("xterm")),
    #([win], "Return", lazy.spawn("gnome-terminal")),

    # Enciende el modo nocturno
    ([win], "m", lazy.spawn("redshift -O 2400")),
    ([win, shift], "m", lazy.spawn("redshift -x")),

    # Captura de pantalla automatica y manual
    ([win], "s", lazy.spawn("scrot")),
    ([win, shift], "s", lazy.spawn("scrot -s")),
    
    # Lanzar VSCode
    ([win], "c", lazy.spawn("code")),
    # Lanzar Intellij IDEA
    ([win], "i", lazy.spawn("idea")),
    # Lanzar Microsoft Teams
    ([win], "t", lazy.spawn("teams")),
    # Lanzar programas de gnome
    ([win, shift], "c", lazy.spawn("gnome-calculator")),
    ([win, shift], "i", lazy.spawn("gnome-control-center")),
    ([win, shift], "p", lazy.spawn("gnome-system-monitor")),

    # Otras Letras Disponibles (a b d g h y u o p ñ x v n)
    #([win], "a", lazy.spawn("")),
    #([win], "b", lazy.spawn("")),
    #([win], "d", lazy.spawn("")),
    #([win], "g", lazy.spawn("")),
    
    # ------------ Configuración de hardware ------------
    # Volumen
    ([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")),
    ([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ 10%-")),
    ([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Brillo
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]