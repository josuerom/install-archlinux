## Pack de Programas Recomendados para que Instales en tu Distribución Arch Linux.
Acabas de entrar a donde algún o algunos programas de la lista te puedan interesar.

#### Instala Yay
***Otro yogur más*** por siglas en ingles (Yet Another Yogurt), es un asistente de instalación de software para todo GNU/Linux, si el programa que deseas no está en [AUR](https://archlinux.org/packages/) no existe para Linux.

Ejecute dentro de > $HOME/
```bash
  cd ~ && git clone https://aur.archlinux.org/yay-git.git && cd yay-git && makepkg -si
```
### Instala todo los programas de un solo tiro
```bash
  yay -S git nodejs htop cmatrix ranger ripgrep brave-bin nerd-fonts-ubuntu-mono ttf-jetbrains-mono ttf-cascadia-code obs-studio libreoffice-fresh-sdk onlyoffice-bin jdk-openjdk neovim visual-studio-code-bin spotify teams notion-app kdocker stacer
```

#### Instala Navegador
***Google Chrome*** es un navegador ligero y muy intuitivo que llama mucho la atención y muchos desarroladores lo utilizan.
```bash
  yay -S google-chrome
  yay -S brave-bin
```

#### Instala Fuentes
La fuente para programar y realizar otra tareas es importante, ya que así te sentirás más agusto al leer y escribirlo, yo recomiento que use alguna de estas tres fuentes muy poderosas (UbuntuMono Nerd Font, JetBrains Mono o Cascadia Code).
```bash
  yay -S nerd-fonts-ubuntu-mono ttf-jetbrains-mono ttf-cascadia-code
```

#### Instala OBS Studio
Si nesecitas algún grabador de pantalla, recomiendo que te instales este.
```bash
  yay -S obs-studio
```

#### Instala Libre Office
***LibreOffice*** es el hermano menor de Microsoft Office pero para trabajar en linux.
```bash
  yay -S libreoffice-fresh-sdk
```

#### Instala OnlyOffice 
```bash
  yay -S onlyoffice-bin 
```

#### Instala Antivirus
```bash
  yay -S libredefender
```

#### Instala OpenJDK Java
```bash
  yay -S jdk-openjdk
```

#### Instala Intellij IDEA
Si trabajas con java y eres fanatico del entorno de desarrollo integrado o IDE Intellij IDEA, pues no esperes más y ¡instalalo ya!.
```bash
  yay -S intellij-idea-community-edition
  yay -S clion
```

#### Instala Visual Studio Code
```bash
  yay -S visual-studio-code-bin
  yay -S sublime-text-4
```

#### Instala Microsoft Teams
```bash
  yay -S teams
```

#### Instala Spotify
```bash
  yay -S spotify
```

#### Instala Notion
```bash
  yay -S notion-app 
```

#### Instala Docker
```bash
  yay -S kdocker
```

#### Instala Stacer
```bash
  yay -S stacer
```