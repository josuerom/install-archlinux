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

#### Establece el idioma y distribución del teclado permanentemente:
```bash
  loadkeys /usr/share/kbd/keymaps/i386/qwerty/la-latin1.map.gz
```

#### Conectate a una red WIFI inalámbrica
Necesitas conexión a internet en tu máquina para poder llevar a cabo las próximas instalaciones. 
```bash
  ip link
  rfkill unblock all
  iwctl--passhrase <clave-wifi> station wlan0 connect <nombre-de-red>
  # verifica si tienes internet con
  ping archlinux.org -c 3
```

#### Verifica si el modo de arranque de tu PC es UEFI o BIOS
Estoy es muy importante, debido a que, está guía de instalación es para máquinas con modo de arranque UEFI ya que al lanzar el sgt comando, me arroja resultados.
```bash
  # si te muestra resultados, es por UEFI
  ls -/sys/firmware/efi/efivars
```

#### Actualiza tu zona horaria
Ajustale la zona horaria a tu máquina con los siguientes comandos, cabe mencionar que todo está configuración la basó en idioma latinoamericano, Bogotá, Colombia.
```bash
  timedatectl set-timezone America/Bogota
  timedatectl status
```

#### Conoce todas las particiones de tu disco duro
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
  swapon  /dev/nombre-particion-swap
  fdisk -l
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
  pacman -S pacman-contrib
  rankmirrors -n 10 /etc/pacman.d/mirrorlist.bak > /etc/pacman.d/mirrorlist
```

#### Instala el Kernel de Linux junto con los programas necesarios
```bash
  # este comando contiene la instalación de kernel
  pacstrap -i /mnt base base-devel linux linux-lts linux-headers linux-firmware
  
  # ahora instalaremos todos los programas y paquetes que utilizaremos
  pacstrap -i /mnt sudo nano neovim code git neofetch network-manager-applet dhcpcd brightnessctl volumeicon cbatticon vlc bluez wpa_supplicant firefox xterm which pulseaudio pavucontrol pamixer htop alacritty ranger rofi scrot redshift qtile feh libnotify notification-daemon xorg-server xorg-xinit unzip picom geeqie
  
  # conozca los archivos de sistemas /root
  ls /mnt
```

#### Genera la tabla del sistema de archivos FSTAB
Este paso es para
```bash
  genfstab -U /mnt >> /mnt/etc/fstab
  cat /mnt/etc/fstab
```

#### Establece una contraseña de usuario y de administrador
```bash
  arch-chroot /mnt
  passwd
  useradd -m <username>
  passwd <username>
  usermod -aG wheel,video,audio,storage <username>
  
  # ejecuta este comando
  EDITOR=nano visudo
  # descomenta la sugiente línea que contiene: # %wheel ALL=(ALL) ALL
  # debajo de ella agregue esto:
  # Defaults timestamp_timeout=0
```

#### Establezca el idioma para el SO Arch Linux
```bash
  # abra el archvip locale.gen y descomente la línea (#es_CO.UTF-8 UTF-8)
  nano /etc/locale.gen
  locale-gen
  echo LANG=es_CO.UTF-8 > /etc/locale.conf
  export LANG= es_CO.UTF-8
```

#### Establezca un nombre para su PC
```bash
  echo <nombre-del-pc> > /etc/hostname
```
  
#### Actualiza tu zona horaria y región
```bash
  ln -sf /usr/share/zoneinfo/America/Bogota /etc/localtime
```

#### Instala el cargador de arranque GRUB
```bash
  lsblk
  mkdir /boot/efi
  mount /dev/nombre-partición-efi-de-100M /boot/efi
  lsblk
  pacman -S grub efibootmgr os-prober networkmanager
  nano /etc/default/grub (descomente la última línea nada más)

  # ahora ejecute este
  grub-install --target=x86_64-efi --bootloader-id=’Arch Linux’ --recheck
  # si ese da algun error entonces ejecute este
  grub-install --target=x86_64-efi --efi-directory=/boot
```
```bash  
  # luego termine de ejecutar estos
  os-prober
  grub-mkconfig -o /boot/grub/grub.cfg
  systemctl enable dhcpcd.service
  systemctl enable NetworkManager.service
  exit
  umount -R /mnt
  reboot
```

#### Una vez te hayas logueado con usuario y contraseña
Debe conectar a tu red WiFi, con el siguiente comando
```bash
  nmcli dev wifi connect <nombre-de-la-red> password <la-clave>
```
Si lo prefieres también puedes actualizar todos los paquetes del sistema
```bash
  sudo pacman -Syys
```

#### Instala el controlador de la tarjeta gráfica Intel
```bash
  sudo pacman -S xf86-video-intel intel-ucode
```

#### Instalar el gestor de Escritorio GNOME junto al gestor de inicio de sesión Lightdm:
En este caso instalaré GNOME ya que es el mismo escritorio que trae ***Ubuntu, Fedora y otras distribuciones GNU/Linux*** por defecto, ejecuta los siguientes comandos para culminar toda la instalación de Arch:
```bash
  sudo pacman -S gnome lightdm lightdm-gtk-greeter
```

Ahora abre el archivo que está en ***/etc/share///***, y modifica la siguentr línea
```bash
  greeter-session = lightdm-gtk-greeter
```

Acto seguido, enciendelo lightdm y reinicia el SO para que veas los cambios
```bash
  sudo systemctl enable lightdm
  reboot
```

Listo, si todo lo realizaste bien, ya tendrías el sistema operativo Arch Linux completamente instalado y funcionando a la perfección, si no pudiste instalarlo la primera vez con ayuda de esta guía medio entendible para los que tienen poco conocimiento de linux, pues contactame vía correo para ayuderte.
```email
  josueromram@outlook.es
```

### Muchas gracias por leerte esta guía de instalación medio entendible.
