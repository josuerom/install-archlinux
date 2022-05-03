## Comandos para Instalar ARCH LINUX en Portátiles LENOVO u otras marcas.

Cordial saludo, en la presente documentación comparto una guía de instalación para ***Arch Linux***, ya que es la distribución ***GNU/Linux*** que me llama más la atención debido a que consume muy pocos MegaBytes(MB) de memoria RAM.

Cabe mencionarle que, los próximos comandos que verás en esta documentación, me funcionaron en mi portátil Lenovo 2021, si tu tienes alguna otra marca de portátiles, que no tengan puertos para Ethernet, el modo de arranque sea UEFI y quieras instalar Arch junto a tu SO Windows, esta guía es para tí y te funcionará.

#### Cambia el tamaño de la fuente de la terminal por el momento de instalación
La fuente que trae la terminal de arch pues es muy pequeña, para ello la podemos poner más grande para que sea más cómoda.
```bash
  setfont ter-132n
```

#### Cambia el idioma del teclado por el momento
Si muy bien usted intentan colocar algún símbolo verá que le aparecerá otro o el símbolo que buscas en esa tecla no está, para ello necesitas que tu teclado hablé el mismo idioma tuyo.
```bash
  loadkeys la-latin1
```

#### Verifica si el modo de arranque de tu PC es UEFI o BIOS
Estoy es muy importante, debido a que, está guía de instalación es para máquinas con modo de arranque UEFI ya que al lanzar el sgt comando, me arroja resultados.
```bash
  # si te muestra resultados, es por UEFI
  ls -/sys/firmware/efi/efivars
```

#### Conectate a una red WIFI inalámbrica
Necesitas conexión a internet en tu máquina para poder llevar a cabo las próximas instalaciones. 
```bash
  ip link
  rfkill unblock all
  iwctl --passphrase <clave-wifi> station wlan0 connect <nombre-de-red>
  # verifica si tienes internet con
  ping archlinux.org -c 3
```

#### Actualiza tu Región
Ajustale la zona horaria a tu máquina con los siguientes comandos, cabe mencionar que todo está configuración la basó en idioma latinoamericano, Bogotá, Colombia.
```bash
  timedatectl set-timezone America/Bogota
  timedatectl status
```

#### Conoce todas las particiones del disco duro
Lista las participaciones de todo tu disco duro
```bash
  lsblk
```

#### Crea las particiones para el funcionamiento del SO Arch Linux.
Esta es la parte más difícil para todos los que quieren instalar ***Arch*** por primera vez. Las siguientes instrucciones son para instalar Arch Linux junto a Windows, función más conocida como ***Dual Boot*** para empezar, debes realizar todo al pie de la letra. Ejecute el comando:
```bash
  # entra al editor de particiones gráfico de Arch:
  cfdisk /dev/<nombre-del-disco-duro-principal>
```

Allí dentro solo debes crear 3 particiones, sin tocar las de Windows, haz lo siguiente.

1. Para la raíz o /root, mínimo dale 15GB ya que el sistema pesará aproximadamente de 6,7GB a 8,5GB, el resto es para los paquetes de actualización del kernel de GNU/Linux. Además, la partición debe ser de tipo Linux filesystem.

2. Para carpeta personal o /home para los archivos personales, descargas, programas, etc. A esa partición si ponle la cantidad que desees, yo te recomiendo que le pongas unos 30GB como mínimo y como máximo lo que desees. Además, esta deber ser de tipo Linux filesystem.

3. Para la memoria de intercambio o /swap, especial para que cuando su memoria RAM tenga muchos procesos ejecutandose, la nueva memoria ram virtual conocida como swap o memoria de intercambio, le ayude a mantener algunos procesos. Te recomiendo que si usas 4GB de ram le pongas 8GB, o si tienes 8GB de ram, le coloques 8GB. Además, es muy importante que esa partición sea de tipo Linux swap.

#### Formatea el sistema de archivo para las nuevas 3 particiones
Añádale el sistema de archivos correspondiente a las particiones.
```bash
  mkfs.ext4  /dev/nombre-particion-root
  mkfs.ext4  /dev/nombre-particion-home
  mkswap  /dev/nombre-particion-swap
  swapon /dev/nombre-particion-swap
  lsblk
```

#### Monta las particiones al sistema
Este paso es para montar las participaciones previamente formateadas en la ruta que deben estar. 
```bash
  mount /dev/nombre-particion-root /mnt
  mkdir /mnt/home
  mount /dev/nombre-particion-home /mnt/home
  lsblk
```

#### Configura los "espejos" más rápidos para el sistema
Esto es más que todo para
```bash
  cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
  ls  /etc/pacman.d
  pacman -Sy
  pacman -S pacman-contrib && rankmirrors -n 10 /etc/pacman.d/mirrorlist.bak > /etc/pacman.d/mirrorlist
```

#### Instala el Kernel de Linux junto con los programas necesarios
```bash
  # este comando contiene la instalación de kernel y otros programas necesarios
  pacstrap -i /mnt linux linux-firmware base base-devel nano neovim code git neofetch network-manager-applet netctl dhcpcd dialog wpa_supplicant brightnessctl volumeicon cbatticon vlc bluez firefox xterm alacritty pulseaudio pavucontrol pamixer htop thunar rofi scrot redshift feh xorg unzip picom geeqie
  # conozca los archivos de sistemas /root
  ls /mnt
```

#### Genera tabla del sistema de archivos FSTAB
El fichero fstab se encuentra comúnmente en sistemas Unix como parte de la configuración del sistema. Lo más destacado de este fichero es la lista de discos y particiones disponibles. En ella se indica cómo montar cada dispositivo y qué configuración utilizar.
```bash
  genfstab -U /mnt >> /mnt/etc/fstab
  cat /mnt/etc/fstab
```

#### Establece una contraseña de administrador y de usuario
```bash
  arch-chroot /mnt
  passwd
  useradd -m <username>
  passwd <username>
  usermod -aG wheel,video,audio,storage <username>
  # ejecute y edite
  EDITOR=nano visudo
  # descomente la sugiente línea: # %wheel ALL=(ALL) ALL
  # debajo de ella agregue esto:
  Defaults timestamp_timeout=0
```

#### Establezca el idioma para el SO Arch Linux
```bash
  # abra el archvip locale.gen y descomente la línea (#es_CO.UTF-8 UTF-8)
  nano /etc/locale.gen
  locale-gen
  echo KEYMAP=la-latin1 > /etc/vconsole.conf
  echo LANG=es_CO.UTF-8 > /etc/locale.conf
  export LANG= es_CO.UTF-8
```

#### Establezca un nombre para su PC
```bash
  echo <nombre-del-pc> > /etc/hostname
```
  
#### Actualiza la hora
```bash
  ln -sf /usr/share/zoneinfo/America/Bogota /etc/localtime
```

#### Instala el cargador de arranque GRUB
```bash
  mkdir /boot/efi
  mount /dev/nombre-partición-efi-de-100M /boot/efi
  # si te arroja error es normal
  
  pacman -S grub efibootmgr os-prober networkmanager
  nano /etc/default/grub
  # descomente la última línea nada más
  
  # ahora ejecute este
  grub-install --target=x86_64-efi --bootloader-id=’Arch Linux’ --recheck
```

```bash  
  # luego termine de ejecutar estos
  os-prober
  grub-mkconfig -o /boot/grub/grub.cfg
  # encienda los servicios
  systemctl enable dhcpcd.service
  systemctl enable NetworkManager.service
  exit
  umount -R /mnt
  reboot
```

### Una vez te hayas logueado con usuario y contraseña

Conectate a tu red WiFi, con el siguiente comando
```bash
  sudo su
  nmcli dev wifi connect <nombre-de-la-red> password <la-clave>
```
Si lo prefieres también puedes actualizar todos los paquetes del sistema
```bash
  pacman -Syys
```

#### Instala los driver de la tarjeta gráfica Intel
```bash
  pacman -S xf86-video-intel intel-ucode
```

#### Instala driver para el TouchPad
```bash
  pacman -S xf86-input-libinput
  cd /etc/X11/xorg.conf.d/
  nano 30-touchpad.conf
  
  # agrege estas líneas
  Section "Inputclass"
    Identifier "devname"
    Driver "libinput"
    Option "Tapping" "on"
    Option "NaturalScrolling" "true"
   EndSection
```

#### Instalar el gestor de Ventanas QTILE junto al gestor de inicio de sesión LIGHTDM:
En este caso se instalará QTILE ya que es el mejor gestor de ventanas para trabajar en Arch que exite hasta el momento en ***GNU/Linux***, más que todo es para el flujo sin tener que usar tanto el mouse, ejecuta los siguientes comandos para culminar esta guía.

Si quieres descargar mi configuración de QTILE, clone este repositorio
```bash
  cd /home/<username>/
  git clone https://github.com/josuerom/arch-linux.git
  mv arch-linux dotfiles
```

Acto seguido, descarga el gestor de ventanas y de sesión, el archivo <lightdm.conf> debe editarlo.
```
  pacman -S qtile lightdm lightdm-gtk-greeter
  nano /etc/lightdm/lightdm.conf
  # en el archivo descomente la línea
  # #greeter-session y agrégue esto
  greeter-session = lightdm-gtk-greeter

  # encienda el servicio y reinicie para que vea los cambios
  systemctl enable lightdm.service
  reboot
```

Y listo, si todo lo realizaste bien, ya tendrías el sistema operativo Arch Linux completamente instalado y funcionando a la perfección, solo te faltaría personalizar el gestor de ventanas ***Qtile*** para que no tengas la pantalla en negro y sin nada.

Pero si no pudiste instalarlo la primera vez con esta ayuda medio entendible para los que no tienen conocimientos de linux, si tu fuiste uno contactame vía email para ayuderte.
```email
  josueromram@outlook.es
```

### Muchas gracias por leerte esta guía de instalación medio entendible.
