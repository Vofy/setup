#!/bin/bash
echo "Napište příkaz pro instalaci balíčku (např. apt install)"
read PACKAGE_MANAGER_INSTALL_COMMAND
sudo $PACKAGE_MANAGER_INSTALL_COMMAND python3-dev python3-devel gcc gcc-c++ alacritty
sudo $PACKGGE_MANAGER_INSTALL_COMMAND fish && set -U fish_greeting
DIR="$(cd "$(dirname "$0")" && pwd)"
ln -sf $DIR/dotfiles/.vimrc $HOME/.vimrc
ln -sf $DIR/dotfiles/.ideavimrc $HOME/.ideavimrc
ln -sf $DIR/dotfiles/qtile/ $HOME/.config/
