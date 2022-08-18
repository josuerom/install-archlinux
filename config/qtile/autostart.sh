# Transparencia
picom &

# Pantalla con HDMI
hdmi=`xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}'`

# Configuración adicional para la pantalla
if [ "$hdmi" = "HDMI-1" ]; then
  xrandr --output eDP-1 --primary --mode 1366x768 --pos 276x1080 --output HDMI-1 --mode 1920x1080 --pos 0x0 &
else
  xrandr --output eDP-1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-1 --off --output DP-1 --off &
fi

# Red volumen y bateria
nm-applet &
volumeicon &
cbatticon &

# Distribución del teclado
setxkbmap latam &

# Dispositivos Automount
udiskie -t &

# Fuentes Java
xsettingsd &

# Wallpaper
nitrogen --restore &

# Overlay Bar
xob-pulse-py | xob -s pulse &
xob-brightness-js | xob -s brightness &