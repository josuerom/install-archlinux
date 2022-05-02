#!/bin/sh

# ajustes para la resulución
xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x1080 --output HDMI-1 --mode 1920x1080 --pos 0x0 &
# fondo de pantalla
feh --bg-scale Imágenes/02.jpg
# icono de bateria en barra de tareas
cbatticon &
# icono de volumen
volumeicon &
# idoma del teclado en español
setxkbmap es &
# efecto de transparencia
picom &
nm-applet &
udiskie -t &