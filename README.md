## Comandos para Instalar ARCH LINUX en Portátiles LENOVO u otras marcas.

Cordial saludo, en la presente documentación comparto una guía de instalación para ***Arch Linux***, ya que es la distribución ***GNU/Linux*** que me llama más la atención debido a que consume muy pocos MegaBytes(MB) de memoria RAM.

Cabe mencionarle que, los próximos comandos que verás en esta documentación, me funcionaron en mi portátil Lenovo 2021, si tu tienes alguna otra marca de portátiles, que no tengan puertos para Ethernet, el modo de arranque sea UEFI y quieras instalar Arch junto a tu SO Windows, esta guía es para tí y te funcionará.

#### Cambia el tamaño de la fuente de la terminal por el momento de instalación
La fuente que trae la terminal de arch pues es muy pequeña, para ello la podemos poner más grande para que sea más cómoda.
```bash
  setfont ter-132n
```

#### Cambia el idioma del teclado para la instalación
Si muy bien usted intentan colocar algún símbolo verá que le aparecerá otro o el símbolo que buscas en esa tecla no está, para ello necesitas que tu teclado hablé el mismo idioma tuyo.
```bash
  loadkeys la-latin1
```

#### Verifica si el modo de arranque de tu PC es UEFI o BIOS
Estoy es muy importante, debido a que, está guía de instalación es para máquinas con modo de arranque UEFI ya que al lanzar el sgt comando, me arroja resultados.
```bash
  # si te muestra resultados este comando, será UEFI,sino BIOS
  ls -/sys/firmware/efi/efivars
```

#### Conectate a una red WIFI inalámbrica
Necesitas conexión a internet en tu máquina para poder llevar a cabo las próximas instalaciones. 
```bash
  ip link
  rfkill unblock all
  iwctl --passphrase <clave-wifi> station wlan0 connect <nombre-de-red>
  # verifica si tienes internet con
  ping 181.237.45.160 -c 4
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
```

#### Monta las particiones al sistema
Este paso es para montar las participaciones previamente formateadas en la ruta que deben estar. 
```bash
  mount /dev/nombre-particion-root /mnt
  mkdir /mnt/home
  mkdir /mnt/boot/efi
  mount /dev/nombre-particion-home /mnt/home
  
  # si te comando te arroja error, no pasa nada y es necesario
  mount /dev/nombre-partición-efi /boot/efi
  # verifica que las nuevas particiones esten montadas con su tipo
  lsblk
```

#### Configure los espejos más rápidos
```bash
  cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
  pacman -Sy
  pacman -S pacman-contrib
  rankmirrors -n 10 /etc/pacman.d/mirrorlist.bak > /etc/pacman.d/mirror list
  cat /etc/pacman.d/mirrorlist
```

#### Instala el Kernel de Linux junto con los programas necesarios
```bash
  # este comando contiene la instalación de kernel
  # los paquetes que no quiera tener no los instale
  pacstrap -i /mnt linux linux-firmware base base-devel nano git network-manager-applet netctl dhcpcd dialog wpa_supplicant vlc firefox alacritty htop unzip
 
 # conozca los archivos de sistemas /root
  ls /mnt
```

#### Genera tabla del sistema de archivos FSTAB
El fichero fstab se encuentra comúnmente en sistemas Unix como parte de la configuración del sistema. Lo más destacado de este fichero es la lista de discos y particiones disponibles. En ella se indica cómo montar cada dispositivo y qué configuración utilizar.
```bash
  genfstab -U /mnt >> /mnt/etc/fstab
  cat /mnt/etc/fstab
```

#### Establece una contraseña de administrador y nombre de usuario
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
  %<username> ALL=(ALL) ALL
```

#### Establezca un nombre para su PC
```bash
  echo <nombre-del-pc> > /etc/hostname
```

#### Establezca el idioma para el SO Arch Linux
```bash
  # busca tu zona horaria en el siguente listado, en mi caso fue: America/Bogota
  timedatectl list-timezones
  timedatectl set-timezone America/Bogota
  timedatectl status
  
  # actualiza tu zona horaria con
  ln -sf /usr/share/zoneinfo/America/Bogota /etc/localtime
  
  # configura el idoma del sistema
  # primero abra el archvio locale.gen y descomente la línea > #es_CO.UTF-8 UTF-8
  nano /etc/locale.gen
  locale-gen
  
  # configura el reloj
  hwclock -w
  
  # verfica si tu fecha y hora es correcta con
  date
```
  
#### Configura el idoma y distribución del teclado en latino permanente
```bash
  echo KEYMAP=latam > /etc/vconsole.conf
  echo LANG=es_CO.UTF-8 > /etc/locale.conf
```

#### Instala el cargador de arranque GRUB y configuralo
```bash
  pacman -S grub efibootmgr os-prober networkmanager
  # descomente la última línea en el archivo grub nada más
  nano /etc/default/grub
  
  # ahora ejecute el comando final
  grub-install --target=x86_64-efi --bootloader-id=’Arch’ --recheck
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

Conectate a tu red WiFi
```bash
  nmcli dev wifi connect <nombre-de-la-red> password <la-clave>
```

#### Instala los driver de la tarjeta gráfica Intel
```bash
  sudo pacman -S xf86-video-intel intel-ucode
```

#### Si prefiere también puede actualizar todos los paquetes del sistema
```bash
  sudo pacman -Sys
```

#### Instala driver para el TouchPad
```bash
  sudo pacman -S xf86-input-libinput
  cd /etc/X11/xorg.conf.d/
  sudo nano 30-touchpad.conf
  
  # agregele estas líneas
  Section "InputClass"
    Identifier "devname"
    Driver "libinput"
    Option "Tapping" "on"
    Option "NaturalScrolling" "true"
   EndSection
```

#### Instala Xorg y Mesa
```bash
  sudo pacman -S xorg-server xorg-xinit mesa mesa-demos
```

#### Instala el Gestor de Ventanas GNOME o QTILE Junto al Gestor de Inicio de Sesión GDM o LIGHTDM:
En este caso se instalará GNOME y QTILE ya que son los mejores gestor de ventanas para trabajar en Arch que exite hasta el momento en ***GNU/Linux***, Qtile es más que todo para el flujo de trabajo sin tener que usar tanto el mouse y GNOME todo lo contrario, ejecuta los siguientes comandos para culminar esta guía.

Si tu deseas tener Arch con el gestor Gnome igual a Ubuntu pues sigue estos pasos.
```
  sudo pacman -S gnome gnome-extra gdm
  # encienda el serviciode inicio de sesión
  sudo systemctl enable gdm.service
  # reinicie para que vea los cambios
  reboot
```

Pero si usted quiere ser un Hacker en con Arch Linux, entonces instale el gestor de escritorio Qtile y Lightdm.


Si quieres clonate mi configuración de QTILE.
```bash
  sudo pacman -S qtile lightdm lightdm-gtk-greeter
  # edite lo siguiente
  sudo nano /etc/lightdm/lightdm.conf
  # en el archivo descomente la línea -> #greeter-session y agréguele esto
  greeter-session = lightdm-gtk-greeter
```

Si instalaste Qtile clonate esta configuración para que se vea mejor
```bash
  cd /home/<username>/
  git clone https://github.com/josuerom/arch-linux.git
  cp -r arch-linux/config/qtile ~/.config/
  reboot
```

Y listo, si todo lo realizaste bien, ya tendrías el sistema operativo Arch Linux completamente instalado y funcionando a la perfección, solo te faltaría personalizar el gestor de ventanas ***Qtile*** ¡si lo instalaste! para que no tengas la pantalla en negro y nada agradable.

Pero si no pudiste instalarlo la primera vez con esta ayuda medio entendible para los que no tienen conocimientos de linux, entonces contactame vía email para brindarte ayuda gratis.
```email
  josueromram@outlook.es
```

### Muchas gracias por leerte esta guía de instalación medio entendible.
