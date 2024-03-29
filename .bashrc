#  author: josuerom date: 20/05/23 13:21
#  ~/.bashrc

[[ $- != *i* ]] && return

export HISTCONTROL=ignoreboth:erasedups

PS1='[\u@\h \W]\$ '

if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi

export BAT_CONFIG_PATH="~/.config/bat/config.conf"

alias cat='bat '
alias rg='batgrep '
alias man='tldr '

alias iso="cat /etc/dev-rel | awk -F '=' '/ISO/ {print $2}'"

bind 'set completion-ignore-case on'

alias probe='sudo -E hw-probe -all -upload'

# Replace ls with exa
alias ls='exa -la --color=always --group-directories-first --icons' # preferred listing
alias la='exa -a --color=always --group-directories-first --icons'  # all files and dirs
alias ll='exa -al --color=always --group-directories-first --icons'  # long format
alias lt='exa -aT --color=always --group-directories-first --icons' # tree listing
alias l='exa -lah --color=always --group-directories-first --icons' # tree listing

#pacman unlock
alias unlock='sudo rm /var/lib/pacman/db.lck'

#available free memory
alias free='free -mt'

#continue download
alias wget='wget -c'

#readable output
alias df='df -h'

#userlist
alias userlist='cut -d: -f1 /etc/passwd'

#Pacman for software managment
alias upall='topgrade'
alias search='sudo pacman -Qs'
alias uninstall='sudo pacman -Rcns'
alias install='sudo pacman -S'
alias linstall='sudo pacman -U'
alias update='sudo pacman -Syyu && flatpak update -y'
alias clrcache='sudo pacman -Scc -y'
alias orphans='sudo pacman -Rns $(pacman -Qtdq)'
alias akring='sudo pacman -Sy archlinux-keyring --noconfirm'

# Paru/Yay stuff
alias pget='paru -S '
alias yayi='yay -S '
alias yayu='yay -R '
alias prem='paru -R '

#Bash aliases
alias jctl='journalctl -p 3 -xb'
alias rbash='source ~/.bashrc'
alias cbash='nvim ~/.bashrc'
alias zreload='cd ~ && source ~/.zshrc'
alias pingme='ping -c64 github.com'
alias cls='clear && neofetch'
alias traceme='traceroute github.com'
alias neo='neofetch'
alias mhacker='cmatrix'
alias ip='ifconfig'
alias comcpp='g++ -Wall -Wextra -Wshadow -Wpedantic -Weffc++ -Wvla -Djosuerom -o ~/workspace/build/cpp-sol.out'
alias runcpp='~/workspace/build/cpp-sol.out'
alias runjava='java'
alias ccf='cd ~/workspace/codeforces/solutions/'
alias cwork='cd ~/workspace/ && ls'
alias tem-cpp='cp -r ~/workspace/templates/tem.cpp A_ && nvim A_'
alias tem-java='cp -r ~/workspace/templates/tem.java A_ && nvim A_'
alias c='clear'
alias e='exit'
alias ..='cd ..'

#hardware info --short
alias hw='hwinfo --short'

## HBlock
alias ublock='sudo hblock'

#youtube-dl
alias yta-best="yt-dlp --extract-audio --audio-format best "
alias ytv-best="yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 "

#GiT  command
alias gi='git init'
alias ga='git add .'
alias gs='git status'
alias gc='git commit -a'
alias gp='git push'
alias gcl='git clone'
alias gl='git pull'
alias glom='git pull origin main'
alias gbr='git branch'
alias gst='git stash'
alias gd='git diff'
alias gch='git checkout'
alias glo='git log --oneline'
#alias token='echo "?"'

#Copy/Remove files/dirs
alias rmd='rm -r'
alias rmf='rm -rf'
alias srm='sudo rm'
alias srmd='sudo rm -r'
alias cpd='cp -R'
alias scpd='sudo cp -R'

#Create file
alias nf='touch'

#nano
alias nz='$EDITOR ~/.zshrc'
alias nbashrc='sudo nano ~/.bashrc'
alias nzshrc='sudo nano ~/.zshrc'
alias nsddm='sudo nano /etc/sddm.conf'
alias pconf='sudo nano /etc/pacman.conf'
alias mkpkg='sudo nano /etc/makepkg.conf'
alias ngrub='sudo nano /etc/default/grub'
alias smbconf='sudo nano /etc/samba/smb.conf'
alias nlightdm='sudo $EDITOR /etc/lightdm/lightdm.conf'
alias nmirrorlist='sudo nano /etc/pacman.d/mirrorlist'
alias nsddmk='sudo $EDITOR /etc/sddm.conf.d/kde_settings.conf'

#cd/ aliases
alias home='cd ~'
alias etc='cd /etc/'
alias copt='cd /opt/'
alias htdocs='cd /opt/lampp/htdocs/ && ls'
alias xampp='cd /opt/lampp/'
alias music='cd ~/Music'
alias vids='cd ~/Videos'
alias config='cd ~/.config'
alias desk='cd ~/Desktop'
alias pics='cd ~/Pictures'
alias down='cd ~/Downloads'
alias docs='cd ~/Documents'
alias sapps='cd /usr/share/applications'
alias lapps='cd ~/.local/share/applications'

#verify signature for isos
alias gpg-check='gpg2 --keyserver-options auto-key-retrieve --verify'

#receive the key of a developer
alias gpg-retrieve='gpg2 --keyserver-options auto-key-retrieve --receive-keys'

#Recent Installed Packages
alias rip="expac --timefmt='%Y-%m-%d %T' '%l\t%n %v' | sort | tail -200 | nl"
alias riplong="expac --timefmt='%Y-%m-%d %T' '%l\t%n %v' | sort | tail -3000 | nl"

#Package Info
alias info='sudo pacman -Si '
alias infox='sudo pacman -Sii '

##Refresh Keys
alias rkeys='sudo pacman-key --refresh-keys'

### HBLOCK Stuff
alias block="sudo hblock"
alias unhblock="hblock -S none -D none"

## login server minutero
alias login-server='ssh minutero@rampart.engworks.tech -p 2233'

#shutdown or reboot
alias reboot='reboot'
alias poweroff='poweroff'
# quit session in KDE Plasma
alias logout='qdbus org.kde.ksmserver /KSMServer logout 0 0 0'

# # ex = EXtractor for all kinds of archives
# # usage: ex <file>
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   unzstd $1    ;;
      *)           echo ''$1' cannot be extracted via ex()' ;;
    esac
  else
    echo ''$1' is not a valid file'
  fi
}

neofetch
