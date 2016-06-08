#!/usr/bin/python

import subprocess
import os
from importlib import import_module
from plugins import *

# from plugins.elf import elf

class Idamous:
    
    def __init__(self):
        """
            Inits the class
        """
        # Change to not being hardcoded later
        self.operating_system = 'linux'
        self.current_file = None
    
    def set_file(self, filename):
        self.current_file = filename
    
    def get_file(self):
        return self.current_file
        
    def _call_shell_function(self, commandName, args):
        """
            Make a call to the terminal and return the output.
        """
        output = subprocess.check_output([commandName].extend(args))
        return output

    def basics(self):
        result = elf.elf.read_header(self)
        result += md5.md5.checksum(self)
        result += sha1.sha1.checksum(self)
        return result

# If you call idamous.py, run this.
if __name__ == '__main__':
    print 'Creating idamous instance'
    idamous = Idamous()
    
    while True:
        try:
            print 'Enter name of binary file: '
            binary = raw_input()
            f = open(binary)
            f.close()
            break
        except IOError:
            print "File %s does not exist. Try again" % binary
        
    idamous.set_file(binary)
    
    elf.elf.test()
    
    #elf.elf.read_header(idamous)
    
    #md5.md5.checksum(idamous)
    
    #sha1.sha1.checksum(idamous)
    
    basic_info = idamous.basics()
    print basic_info