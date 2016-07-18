#!/bin/bash

sudo apt-get update
sudo apt-get install python python-pip graphviz
if command -v r2 2>/dev/null; then
	echo "Radare is already installed"
else
    sudo git clone https://github.com/radare/radare2 /usr/bin/radare
    sudo /usr/bin/radare/sys/install.sh
fi

sudo pip install peewee python-magic pyreadline r2pipe pydot networkx

################
# Install Angr #
################
read -p "Would you like to install Angr? [Y/n] " -n 1 -r
echo # New line

if [[ $REPLY =~ ^[Yy]$ ]]
then
    sudo apt-get install python-dev libffi-dev build-essential virtualenvwrapper
    sudo pip install -I --no-use-wheel angr-only-z3-custom
    sudo pip install angr # This does NOT create the virtual environment recommended by the angr team
fi
