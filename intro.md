# FoRREST
A Framework of Robust Reverse Engineering Software Tools

Version 0.8

## Overview
The purpose of this project is to create a binary executable analysis framework that
combines existing tools into one package. It also makes it easier to create or
install tools into the framework for use.

## Background
This project was started as part of a National Science Foundation Foundation funded research experience for undergraduates (REU) program at Wright State University in Dayton, Ohio.

FoRREST is currently designed for Linux

## Requirements
* Python 2.7
* python-magic
* pyreadline
* [peewee](https://github.com/coleifer/peewee)
* [Radare2](https://github.com/radare/radare2)
* angr
  * [angr-utils](https://github.com/axt/angr-utils) \(necessary files included already\)
  * pydot
  * networkx
  * graphviz

## Installation
* Clone the project from [https://github.com/drsutherin/FoRREST](https://github.com/drsutherin/FoRREST)
* cd into the FoRREST directory
* Run ```install.sh```

During the installation, you will be prompted as to whether you want to install angr.  This is to allow for a shorter installation time in the event that you only plan to use the lower level functions (e.g. using FoRREST as an introduction to reverse engineering).

####A Note on angr
On angr's [installation page](http://docs.angr.io/INSTALL.html), they recommend using a Python virtual environment because they have their own versions of z3 and pyvex.  We do not currently do this in FoRREST, and the installation script will install the angr-custom versions of those programs.

At this point, we are not offering support for FoRREST while running angr in a virtual environment.  However, if you would like to install it in a virtual environment, following these instructions should help you avoid some common problems when installing angr:
* Install dependencies:
  * ```sudo apt-get install python-dev libffi-dev build-essential virtualenvwrapper```
* Make sure virtualenvwrapper is callable from bash
  * ```whereis virtualenvwrapper```
  * ```sudo chmod +x PATH/TO/virtualenvwrapper.sh```
  * Add the following to ```~/.bashrc```:
    * ```export WORKON_HOME=$HOME/.virtualenvs```
    * ```source PATH/TO/virtualenvwrapper.sh```
  * Then, ```source ~/.bashrc```
* Install several angr dependencies individually (as they tend to cause errors)
  * ```sudo apt-get install -I --no-use-wheel capstone angr-only-z3-custom```
* Finally, ```mkvirtualenv angr && pip install angr```


## Running
To run the program with the command line interface, from the root directory:

```
python main.py
```

## Extending
To extend the program, just import FoRREST into Python

```
~$ python
>>> from FoRREST import FoRREST
```


