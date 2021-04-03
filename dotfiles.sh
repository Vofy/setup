#!/bin/bash
echo "Napište příkaz pro instalaci balíčku (např. apt install)"
read PACKAGE_MANAGER_INSTALL_COMMAND
sudo $PACKAGE_MANAGER_INSTALL_COMMAND python3-dev python3-devel gcc gcc-c++
DIR="$(cd "$(dirname "$0")" && pwd)"
ln -sf $DIR/.vimrc $HOME/.vimrc
