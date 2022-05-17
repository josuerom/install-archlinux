<div align="center">
<p>
    <a>
      <img alt="Linux" src="https://img.shields.io/badge/Linux-%23.svg?style=flat-square&logo=linux&color=FCC624&logoColor=black" />
    </a>
    <a>
      <img alt="macOS" src="https://img.shields.io/badge/macOS-%23.svg?style=flat-square&logo=apple&color=000000&logoColor=white" />
    </a>
    <a>
      <img alt="Windows" src="https://img.shields.io/badge/Windows-%23.svg?style=flat-square&logo=windows&color=0078D6&logoColor=white" />
    </a>
    <a href="https://github.com/josuerom/nvim-config/network">
      <img alt="Forks" src="https://badgen.net/github/forks/josuerom/nvim-config">
    </a>
    <a href="https://github.com/josuerom/nvim-config/stargazers">
      <img alt="Stars" src="https://badgen.net/github/stars/josuerom/nvim-config">
    </a>
    <a href="https://github.com/neovim/neovim/releases/tag/stable">
      <img src="https://img.shields.io/badge/Neovim-0.6.1-blueviolet.svg?style=flat-square&logo=Neovim&logoColor=green" alt="Neovim minimum version"/>
    </a>
</p>
</div>

<H1 align="center">Guía de Instalación y Configuración para Neovim, GNU/Linux - Mayo, 2022.</H1>

<p align="center" width="0">
   <img align="center" width="645" src="https://github.com/josuerom/nvim-config/blob/main/.config/screenshot/neovim-logo-shadow.png">
</p>

<p align="center">
<img src="https://github.com/josuerom/nvim-config/blob/main/.config/screenshot/2022-02-26_18-34-31_Trim.gif" width="800">
</p>

## Introducción.
El presente proyecto describe el proceso que debes seguir para personalizar e instalar **NEOVIM** en su versión más reciente a tu fecha; proyecto realizado tras la devaluación e ineficiencia de instalaciones que hay sobre neovim en español para la distribución **Arch Linux** o cualquier otra, gran parte de los programadores profesionales más exitosos, hoy utilizan este editor de texto/código muy profesional. Asimismo éste estudio de elaboración propia revela la calidad de instalación, configuración y personalización. Para una mejor comprensión de la guía enfoquese y sobre todo descargue cada una de las herramientas inicializadas a continuación:

## Herramientas necesarias.

1. Instalar **Neovim**
2. Instalar **Git**
3. Instalar **Node.js**
4. Clonar/Descargar este repositorio
5. Instalar gestor de plugins **vim plug**

**Tenga en cuenta que:** para instalar Neovim, si o si necesitarás utilizar todas esas 5 herramientas, para ello aquí conocerás el paso a paso para instalar cada una correctamente sin errores ni falsa información.

# Paso a paso para la instalación de NeoVim.
### Paso No. 1. Instalar Neovim.
Para llevar a cabo la instalación copie y pegue el siguiente comando en su terminal, pero está guía la baso en Arch Linux.
```bash
   sudo pacman -S neovim
```
### Paso No. 3. Instalar Git.
Git es un software de control de versiones diseñado por **Linus Torvalds** quién es él mismo creador del Sistema Operativo **GNU-LINUX**, fue pensado en la eficiencia, la confiabilidad y compatibilidad para mantenimientos de versiones; para realizar la instalación de git ejecute el siguiente comando.
```bash
   sudo pacman -S git
```

### Paso No. 4. Instalar Node.js.
**Node.js** es un entorno en tiempo de ejecución multiplataforma, de código abierto, para la capa del servidor basado en el lenguaje de programación JavaScript, en pocas palabras, es un programa el cual permite interpretar o ejecutar archivos javascript y TypeScript sin necesidad de correrlo en el navegador, es por eso que Node.js integra su consola; pero esto es siempre y cuando valles a trabajar con **ALGUNOS DE ELLOS**, si tu no lo dominas o no te interesa trabajar con el *"pues no lo instales y ya"*. Por otra parte, si no lo instalas cada vez que abras neovim te saldrá un aviso en rojo pidiendote que instales Node.js, pero no te preocupes de que podrás utilizar neovim sin problema alguno. Ejecute.
```bash
   sudo pacman -S nodejs
```
### Paso No. 5. Clonar/Descarga este repositorio.
Esta es la personalización que actualmente tengo en neovim:

<p align="center" width="0">
   <img align="center" src="https://github.com/josuerom/nvim-config/blob/main/.config/screenshot/nvim-completo.png">
</p>

``` bash
mkdir ~/.config/nvim && git clone https://github.com/josuerom/nvim-linux.git ~/.config/nvim
```

**PREGUNTA:** ¿Te gustaría tener neovim como lo tengo yo?. Si tu respuesta es un **SÍ** deberás descargarte los archivos de este repositorio ya que son necesarios para que tu Neovim tenga una buena interfaz bacana y las mismas funcionalidades que manejo como: atajos y plugins. Una vez se haya descargado debes extraer el archivo _(nvim-config-windows7-8-10-11-nvim.zip)._ Luego de ello, la carpeta extraída obligatoriamente cambiale el nombre por: **nvim** (en minúsculas).

Ahora bien, corta o copia esa carpeta renombrada 'nvim'. A continuación, dirígete a la siguiente ruta en el Explorador de Archivos: **C:\Users/TuNombreDeUsuario\AppData\Local\** cuando estes ubicado ahí pegas la carpeta. OJO que si no pegas la carpeta en esa ruta que te dije, no podrás abrir NEOVIM.

Para abrir neovim lleva a cabo un comando sencillo en la _Consola/Terminal PowerShell o Símbolo del Sistema_, debes ubicarte en la ruta donde colocaron neovim. La ruta tuya es, ¡la misma mía solo que cambia el nombre de usuario y debes entrar a carpeta nvim! **C:\Users\josue\AppData\Local\nvim\**. Cuando estes ahí debes ingresar el siguiente comando y presionar enter:

```bash
nvim init.vim
``` 

Añado captura de pantalla, por sino me entendiste muy bien, me referia a está:

<p align="center" width="0">
   <img align="center" src="https://github.com/josuerom/nvim-config/blob/main/.config/screenshot/init-vim.png">
</p>

Luego de ejecutar el comando, te arrojará muchos errores pero _NO TE ASUSTES NI DEPRIMAS_ que son normales las primeras veces que lo ejecutas, aparecen porque los plugins no se han instalado. Y deben ser éstos mismos errores los que te aparezcan allá:

<p align="center" width="0">
   <img align="center" src="https://github.com/josuerom/nvim-config/blob/main/.config/screenshot/errores-normales.png">
</p>

Para saltar esos errores puedes presionar varias veces la tecla **Enter** o solo una vez la tecla **Esc**, nada más faltaría instalar el gestor de plugins **vim plug** para que así culmines con el último paso.

### Paso No. 6. Instalar el gestor de plugins VIM PLUG
**Vim plug** es un administrador de plugins para el editor de texto vim y neovim minimalista, de código abierto creado por **junegunn** hace tiempo. Además es totalmente libre de uso. Una de sus principales y más conmovedores funcionalidades es que puede instalar, actualizar y desinstalar complementos en paralelo. Crea clones para minimizar el uso de espacio del disco y el tiempo de descarga; para realizar una descarga limpia y ligera. Ejecuta en la pestaña PowerShell abierta como administrador, el siguiente comando:

```bash
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
``` 

Ese comando creará unos ficheros y archivos como **plug.vim** en la ruta: **C:\Users\TuNombreDeUsuario\AppData\Local\nvim-data\site\autoload\plug.vim**, que nos permitirá instalar los plugins, etc... Si no ejecutas el comando no podrás obtener la misma personalización que tengo yo. 

Continuando con esta super guía de instalación, en la ventana principal o ventana sin nada de nvim escribe el comando que vez debajo de esta línea _tal cual como lo escribí yo_, recuerda que nvim debe estar en modo **NORMAL:** para que te funcione.
> :PlugInstall

Añado captura de pantalla:

<p align="center" width="0">
   <img align="center" src="https://github.com/josuerom/nvim-config/blob/main/.config/screenshot/pluginstall.png">
</p>

Así podrás instalar todos los plugins que manejo a diario, añado otra captura guía.

<p align="center" width="0">
   <img align="center" src="https://github.com/josuerom/nvim-config/blob/main/.config/screenshot/plugins-instalados.png">
</p>

Después de que hayan terminado todas las descargas y quieras conocer los cambios efectuados en tu editor. En modo **NORMAL** presiona las teclas:
> space + x
O cierra y vuelve a entrar.

El comando cerrará neovim completamente. Para que tú luego, lo vuelvas a abrir. ¡Si por si acaso usted no llega a recordar como abrirlo!. Ingresa el siguiente comando en la terminal pero para que te funcione ubicate en misma ruta que antes **C:\Users/TuNombreDeUsuario\AppData\Local\nvim\**. OK posicionado/a en esa ruta, ahora si escribe: 'nvim init.vim'.

En términos generales, veraz el cambio justo como en las imágenes que proporcioné al final de esta guía; cabe mencionar que, si deseas cambiar el tema u otra cosas que no te guste, deberás buscar como realizarlo.

<p align="center" width="0">
   <img align="center" src="https://github.com/josuerom/nvim-config/blob/main/screenshot/nvim-init-vim.png">
</p>

<p align="center" width="0">
   <img align="center" src="https://github.com/josuerom/nvim-config/blob/main/.config/screenshot/nvim-nerdtree_java.png">
</p>

### ¿Necesitas ayuda?, entonces contactate conmigo vía email.
```email
josueromram@outlook.es
```

### Dejaré el proyecto hasta acá, realizaré una pausa por varios días para luego optimizar aún más la configuración convertiendo nvim en un IDE asombroso.
<p align="center" width="0">
   <img align="center" width="45" src="https://github.com/josuerom/nvim-config/blob/main/.config/screenshot/neovim-mark-flat.png">
</p> 
