#!/usr/bin/python

import subprocess
import os
from plugins import *

class Idamous:
    
    def __init__(self):
        """
            Inits the class
        """
        # Change to not being hardcoded later
        self.operating_system = 'linux'
        self.current_file = None
        self.raw = raw.File.File(self)
        self.extract = extract.Extract.Extract(self)
        self.interpret = interpret.Interpret.Interpret(self)
    
    def set_file(self, params):

        try:
            f = open(params[0])
            f.close()
            self.current_file = params[0]
            print "File %s loaded successfully." % params[0]
        except IOError:
            print "That file does not exist, please try again."

        if type(params) == str:
            self.current_file = params
        else:
            self.current_file = params[0]
    
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
                "idamous.set_file(<filename>)"
        
        return output
        
    def get_help(self, params = None):
        f = open("help.txt")
	for line in f:
		print line
    
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
        

def start_shell():
    print ""
    print "IDAMOUS:  Integrated Framework for Reverse Engineering Software"
    print "---------------------------------------------------------------"
    print "Begin by loading your binay with the 'load [yourfile]' command."
    print "Type 'help' to see all available commands!"
    print ""
    
    idamous = Idamous()
    
    should_continue = True
    quit = [
        'quit',
        'exit'
    ]
    
    while should_continue:
        cmd = raw_input("Idamous> ")
    
        if cmd.lower() in quit:
            should_continue = False
        else:
            func = cmd.split()[0]
            params = cmd.split()[1:]
            
            if func == "help": func = "get_help"
            
	    if func == "load": func = "set_file"
	    
            if func in dir(idamous):
                func = getattr(idamous, func)
                try:
                    print func(params)
                except Exception as e:
                    print '[-] function failed to run.'
                    print e
            else:
                print "[-] That command does not exist!"

# If you call idamous.py, run this.
if __name__ == '__main__':
    # start_shell()
    idamous = Idamous()
    idamous.set_file('test_binaries/custom_binaries/generate_fib.out')
    print idamous.get_raw_metadata()
    print idamous.get_extracted_data()
    print idamous.get_interpreted_data()
