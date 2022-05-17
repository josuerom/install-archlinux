# Transparence
picom &

# Screens
hdmi=`xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}'`

if [ "$hdmi" = "HDMI-1" ]; then
  xrandr --output eDP-1 --primary --mode 1366x768 --pos 276x1080 --output HDMI-1 --mode 1920x1080 --pos 0x0 &
else
  xrandr --output eDP-1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-1 --off --output DP-1 --off &
fi

# Network
nm-applet &
volumeicon &
cbatticon &
# Keyboard Layout
setxkbmap latam &
# Automount Devices
udiskie -t &
# Java Fonts
xsettingsd &
# Wallpaper
nitrogen --restore &
# Overlay Bar
xob-pulse-py | xob -s pulse &
xob-brightness-js | xob -s brightness &
