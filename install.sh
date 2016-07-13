#!/bin/bash

sudo apt-get update
sudo apt-get install python python-pip graphviz
sudo git clone https://github.com/radare/radare2 /usr/bin/radare
sudo /usr/bin/radare/sys/install.sh

sudo pip install peewee
sudo pip install python-magic
sudo pip install pyreadline
sudo pip install r2pipe
sudo pip install pydot
sudo pip install networkx

sudo apt-get install python-dev libffi-dev build-essential virtualenvwrapper
sudo pip install -I --no-use-wheel angr-only-z3-custom
mkvirtualenv angr && pip install angr # this may need to move up 2 lines
