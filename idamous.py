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
        self.result_directory = None
    
    def set_file(self, filename):
        self.current_file = filename
    
    def get_file(self):
        return self.current_file

    def set_result_directory(self, dir):
        self.result_directory = dir

    def get_result_directory(self):
        return self.result_directory

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
    
    # Allow user to specify file to test
    while True:
        try:
            print 'Enter name of binary file: '
            binary = raw_input()
            f = open(binary)
            f.close()
            break
        except IOError:
            print "File %s does not exist. Try again" % binary
    
    # Creates a directory for the results of the Idamous tests
    idamous.set_file(binary)
    if "." in binary:
        splitFile = binary.split(".")[-2]
        splitFile = splitFile.split("/")[-1]
    
    idamous.set_result_directory("./results/" + splitFile)
    # This could be dangerous...
    subprocess.Popen(["rm", "-rf", idamous.get_result_directory()])
    subprocess.Popen(["mkdir", idamous.get_result_directory()])

    # Run some test functions
    raw_data = raw.File.File(idamous.get_file())
    
    print 'Filename:', raw_data.get_name()
    print 'File extension:', raw_data.get_extension()
    print 'File size:', raw_data.get_size()
    print 'File inode:', raw_data.get_inode()
    print 'File path:', raw_data.get_path()
    print 'File MD5:', raw_data.get_md5()
    print 'File SHA1:', raw_data.get_sha1()
    
    extracted_data = extract.Extract.Extract(idamous.get_file())
    
    print 'Filetype:', extracted_data.get_filetype()

