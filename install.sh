#!/bin/bash
echo "Napište příkaz pro instalaci balíčku (např. apt install)"
read PACKAGE_MANAGER_INSTALL_COMMAND
sudo $PACKAGE_MANAGER_INSTALL_COMMAND python3-devel gcc gcc-c++ htop ncdu 
sudo $PACKGGE_MANAGER_INSTALL_COMMAND fish && set -U fish_greeting
