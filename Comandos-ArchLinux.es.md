# Guía de Comandos en Arch Linux

### Comandos para el sistema.
La siguiente serie de comandos que veráz, son el uso correcto de el paquete PACMAN y YAY.

```bash
# Actualizar el sistema
sudo pacman -Syu
yay -Syu

# Actualiza el sistema además de los paquetes AUR
yay -Syua

# Sincroniza los paquetes de la base de datos
sudo pacman -Sy 
yay -Sy

# Fuerza la sincronización de los paquetes de la base de datos
sudo pacman -Syy 
yay -Syy 

# Permite buscar un paquete en los repositorios
sudo pacman -Ss paquete 
yay -Ss paquete

# Obtiene información de un paquete que está en los repositorios
sudo pacman -Si paquete 
yay -Si paquete 


sudo pacman -Qi paquete # Muestra la información de un paquete instalado
yay -Qi paquete # Muestra la información de un paquete instalado

sudo pacman -S paquete # Instalar y/o actualizar un paquete
yay -S paquete # Instalar y/o actualizar un paquete

sudo pacman -R paquete # Eliminar un paquete
yay -R paquete # Eliminar un paquete

sudo pacman -U /ruta/hacia/el/paquete # Instalar un paquete local
yay -U /ruta/hacia/el/paquete # Instalar un paquete local

sudo pacman -Scc # Limpiar la caché de los paquetes
yay -Scc # Limpiar la caché de los paquetes

sudo pacman -Rc paquete # Eliminar un paquete y sus dependencias
yay -Rc paquete # Eliminar un paquete y sus dependencias

sudo pacman -Rnsc paquete # Eliminar un paquete, sus dependencias y configuraciones
yay -Rnsc paquete # Desintala un paquete, sus dependencias y configuraciones

sudo pacman -Qdt #Muestra paquetes huérfanos
yay -Qdt #Muestra paquetes huérfanos
```
### Uso rm
```bash
# crear archivo
touch ejemplo.txt

# mover archvios o carpetas
mv /ruta-del-fichero-o-archivo/

# renombra algun archivo o capeta
mv /ruta-del-archivo/ nombre-nuevo

# borra cualquier carpeta, archivo del sistema
rm -rf /ruta-del-archivo-o-carpeta/

```
