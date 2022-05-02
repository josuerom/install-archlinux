############################################################
# ~/.bashrc
############################################################

# Distribute bashrc into smaller, more specific files
source ~/.config/dotfiles/bash/configs/alias
source ~/.config/dotfiles/bash/configs/git

# ${HOME}/.bashrc: executed by bash(1) for non-login shells.
# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# User Info
export USERNAME="josuerom"
export NICKNAME="JR2"

# Welcome message
echo -ne "Buen día, $NICKNAME! Hoy es "; date '+%A, %-d de %B %Y'
echo -e "¡Este es tu momento Hackermen :)!";
echo