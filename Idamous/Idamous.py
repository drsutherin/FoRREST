#!/usr/bin/python

import subprocess
import os
from plugins import *
import sys

class Idamous:

    def __init__(self, filename=None):
        """
            Inits the class
        """
        # Change to not being hardcoded later
        self.operating_system = 'linux'
        self.current_file = filename
        self.raw = raw.Raw.Raw(self)
        self.extract = extract.Extract.Extract(self)
        self.interpret = interpret.Interpret.Interpret(self)
    
    def set_file(self, params):
        if type(params) == str:
            filename = params
        else:
            filename = params[0]
        
        if (os.path.isfile(filename)):
            self.current_file = filename
        else:
            print "[-] That file does not exist!"
        
    
    def get_file(self, params = None):
        return self.current_file
        
    def get_raw_data(self, params = None):
        output = {}

        if self.current_file:
            output['name'] = self.raw.get_name()
            output['extension'] = self.raw.get_extension()
            output['size'] = self.raw.get_size()
            output['md5'] = self.raw.get_md5()
            output['sha1'] = self.raw.get_sha1()
            output['sha256'] = self.raw.get_sha256()
        else:
            print "No file selected! Please select with",\
                "load [filename]"

        return output
        
    def get_extracted_data(self, params = None):
        output = {}
        
        if self.current_file:
            output['type'] = self.extract.get_filetype()
            output['version'] = self.extract.get_version()
            output['architecture'] = self.extract.get_architecture()
            output['compiler'] = self.extract.get_compiler()
            output['sections'] = self.extract.get_sections()
        else:
            print "No file selected! Please select with",\
                "load [filename]"
        
        return output
        
    def get_interpreted_data(self, params = None):
        output = {}
        
        if self.current_file:
            output['opcodes'] = self.interpret.get_opcodes()
            output['strings'] = self.interpret.get_strings()
            output['imports'] = self.interpret.get_imports()
            output['exports'] = self.interpret.get_exports()
            output['header_information'] = self.interpret.get_header_information()
        else:
            print "No file selected! Please select with",\
                "load [filename]"
        
        return output
    
    # Add test to make sure the file is loaded    
    def get_strings(self, params = None):
        output = self.interpret.get_strings()
        return output

    def get_help(self, params = None):
        with open('help.txt', 'r') as f:
            print f.read()
    
    def _shell(self, commandName, args, stdin=None):
        """
            Make a call to the terminal and return the output.
        """
        cmd = [commandName]
        if type(args) == str:
            cmd.append(args)
        else:
            cmd.extend(args)
            
        print 'running', cmd
        
        if stdin:
            out, err = subprocess.Popen(cmd, stdin=stdin, stdout=subprocess.PIPE).communicate()
        else:
            out, err = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()
        
        if out: out = out.splitlines()
        if err: err = err.splitlines()
        
        return out, err
        
    def _shell_std(self, commandName, args, stdin=None):
        """
            Make a call to the terminal and return the output.
        """
        cmd = [commandName]
        if type(args) == str:
            cmd.append(args)
        else:
            cmd.extend(args)
            
        print 'running', cmd
        
        if stdin:
            out = subprocess.Popen(cmd, stdin=stdin, stdout=subprocess.PIPE)
        else:
            out = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            
        return out.stdout

