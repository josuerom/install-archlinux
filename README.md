## Comandos para Instalar ARCH LINUX en Portátiles LENOVO u otras marcas.

Cordial saludo, presento esta pequeña guía de instalación para ***Arch*** ya que es el sistema operativo GNU/Linux que me llama más la atención debido a que consume poca memoria muy poco MB de memoria RAM.

#### Cambia el tamaño de la fuente de la terminal por el momento de instalación:
```bash
  setfont ter-132n
```

#### Cambia el idioma del teclado por el momento:
```bash
  loadkeys la-latin1
```

#### Establece el idioma y distribución del teclado permanentemente:
```bash
  loadkeys /usr/share/kbd/keymaps/i386/qwerty/la-latin1.map.gz
```

#### Conectate a una red WIFI inalámbrica: 
```bash
  ip link
  rfkill unblock all
  iwctl--passhrase <clave-wifi> station wlan0 connect <nombre-de-red>
  # verifica si tienes internet con
  ping archlinux.org -c 3
```

#### Verifica si el modo de arranque de tu PC es UEFI o BIOS:
```bash
  # si al ejecutar este comando te arroja resultados, quiere decir que tu maquina es por UEFI
  ls -/sys/firmware/efi/efivars
```

#### Conoce todas las particiones de tu disco duro:
```bash
  # lista las particiones de tu disco duro
  lsblk
```

#### Entra al editor de particiones gráfico de Arch:
```bash
  cfdisk /dev/<nombre-del-disco-duro-principal>
```

#### Actualiza tu zona horaria:
```bash
  timedatectl list
  timedatectl set-timezone America/Bogota
  timedatectl status
```

#### Crea las particiones para el funcionamiento del SO Arch Linux.
Esta es la parte más difícil para todos los que quieren instalarlo por primera vez. Las siguientes instrucciones son para instalar Arch Linux junto a Windows, función más conocida como Dual Boot para empezar, debes realizar todo al pie de la letra. Ejecute el comando:
```bash
  cfdisk
```

Allí dentro solo debes crear 3 particiones, sin tocar las de Windows, haz lo siguiente.

1. Para la raíz o /root, mínimo dale 15GB ya que el sistema pesará aproximadamente de 6,7GB a 8,5GB, el resto es para los paquetes de actualización del kernel de GNU/Linux. Además, la partición debe ser de tipo Linux filesystem.

2. Para carpeta personal o /home para los archivos personales, descargas, programas, etc. A esa partición si ponle la cantidad que desees, yo te recomiendo que le pongas unos 30GB como mínimo y como máximo lo que desees. Además, esta deber ser de tipo Linux filesystem.

3. Para la memoria de intercambio o /swap, especial para que cuando su memoria RAM tenga muchos procesos ejecutandose, la nueva memoria ram virtual conocida como swap o memoria de intercambio, le ayude a mantener algunos procesos. Te recomiendo que si usas 4GB de ram le pongas 8GB, o si tienes 8GB de ram, le coloques 8GB. Además, es muy importante que esa partición sea de tipo Linux swap.

#### Formatea el sistema de archivo para las nuevas 3 particiones:
```bash
  mkfs.ext4  /dev/nombre-particion-root
  mkfs.ext4  /dev/nombre-particion-home
  mkswap  /dev/nombre-particion-swap
  swapon  /dev/nombre-particion-swap
  fdisk -l
```

#### Monta las particiones al sistema: 
```bash
  mount /dev/nombre-particion-root /mnt
  mkdir /mnt/home
  mount /dev/nombre-particion-home /mnt/home
  lsblk
```

#### Configura los "espejos" más rápidos para el sistema: 
```bash
  cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
  ls  /etc/pacman.d
  pacman -Sy 
  pacman -S pacman-contrib
  rankmirrors -n 10 /etc/pacman.d/mirrorlist.bak > /etc/pacman.d/mirrorlist
```

#### Instala el Kernel de Linux junto a unos programas necesarios.
```bash
  # el siguiente es un solo comando junto, los paquetes (qtile, ranger y redshift) son opcionales
  pacstrap -i /mnt base base-devel linux linux-lts linux-headers linux-firmware sudo nano code git
  neofetch network-manager-applet dhcpcd brightnessctl volumeicon cbatticon lxappearance nitrogen vlc
  bluez wpa_supplicant firefox htop alacritty ranger rofi scrot redshift qtile
  
  # luego que termine, ejecute el sgt comando para conocer los archivos del sistema operativo
  ls /mnt
```

#### Genera la tabla del sistema de archivos FSTAB:
```bash
  genfstab -U /mnt >> /mnt/etc/fstab
  cat /mnt/etc/fstab
```

#### Establece una contraseña de usuario y de administrador: 
```bash
  arch-chroot /mnt
  passwd
  useradd -m <username>
  passwd <username>
  usermod -aG wheel,video,audio,storage <username>
  
  # ejecuta este comando
  EDITOR=nano visudo
  # y descomenta la sugiente línea: (# %wheel ALL=(ALL) ALL)
  # debajo de ella agregue esto: Defaults timestamp_timeout=0
```

#### Establezca el idioma para el SO Arch Linux:
```bash
  # abra el archvip locale.gen y descomente la línea (#es_CO.UTF-8 UTF-8)
  nano /etc/locale.gen
  locale-gen
  echo LANG=es_CO.UTF-8 > /etc/locale.conf
  export LANG= es_CO.UTF-8
```

#### Establezca un nombre para su PC:
```bash
  echo <nombre-del-pc> > /etc/hostname
```
  
#### Actualiza tu zona horaria y región:
```bash
  ln -sf /usr/share/zoneinfo/America/Bogota /etc/localtime
```

#### Instala el cargador de arranque GRUB:
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

#### Una vez te hayas logueado con usuario y contraseña, debes:
```bash
  # conectate a tu red WIFI
  nmcli dev wifi connect <nombre-de-la-red> password <la-clave>
  # descarga/actualiza todos los paquetes necesarios
  sudo pacman -Syys
```

#### Instala el controlador de la tarjeta gráfica para Intel:
```bash
  sudo pacman -S xf86-video-intel intel-ucode
```

#### Instala Xorg y Mesa:
```bash
  sudo pacman -S xorg-server xorg-xinit mesa mesa-demos
```

#### Instalar el gestor de Escritorio GNOME y el gestor de inicio de sesión GDM:
En este caso instalaré GNOME ya que es el mismo escritorio que trae ***Ubuntu, Fedora y otras distribuciones GNU/Linux*** por defecto, ejecuta los siguientes comandos para culminar toda la instalación de Arch:
```bash
  sudo pacman -S gnome gnome-extra gdm
  systemctl enable gdm.service
  reboot
```

Listo, si todo lo realizaste bien, ya tendrías el sistema operativo Arch Linux completamente instalado y funcionando a la perfección, si no pudiste instalarlo a la primera con ayuda de esta guía, contactame para ayuderte

### Muchas gracias por leerte esta guía de instalación medio entendible.
