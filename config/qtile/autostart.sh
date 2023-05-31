# Efecto de transparencia
picom &

# Ajuste de pantalla por HDMI
hdmi=`xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}'`
# Configuración adicional para la pantalla
if [ "$hdmi" = "HDMI-1" ]; then
  xrandr --output eDP-1 --primary --mode 1366x768 --pos 276x1080 --output HDMI-1 --mode 1920x1080 --pos 0x0 &
else
  xrandr --output eDP-1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-1 --off --output DP-1 --off &
fi

# Red, volumen y bateria
nm-applet &
volumeicon &
cbatticon &
# Distribución del teclado
setxkbmap latam &
# Dispositivos automático
udiskie -t &
# Fuentes Java
xsettingsd &
# Fondo de pantalla
nitrogen --restore &
# Barra superpuesta
xob-pulse-py | xob -s pulse &
xob-brightness-js | xob -s brightness &
