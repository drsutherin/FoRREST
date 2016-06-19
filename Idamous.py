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
    
    def set_file(self, params):
        if type(params) == str:
            self.current_file = params
        else:
            self.current_file = params[0]
    
    def get_file(self, params = None):
        return self.current_file
        
    def get_raw_metadata(self, params = None):
        output = {}

        if self.current_file:
            raw_data = raw.File.File(self)

            output['name'] = raw_data.get_name()
            output['extension'] = raw_data.get_extension()
            output['size'] = raw_data.get_size()
            output['md5'] = raw_data.get_md5()
            output['sha1'] = raw_data.get_sha1()
            output['sha256'] = raw_data.get_sha256()
        else:
            print "No file selected! Please select with",\
                "idamous.set_file(<filename>)"

        return output
        
    def get_extracted_data(self, params = None):
        output = {}
        
        if self.current_file:
            extracted_data = extract.Extract.Extract(self)
            output['type'] = extracted_data.get_filetype()
            output['version'] = extracted_data.get_version()
            output['architecture'] = extacted_data.get_architecture()
            output['compiler'] = extracted_data.get_compiler()
            output['sections'] = extracted_data.get_sections()
        else:
            print "No file selected! Please select with",\
                "idamous.set_file(<filename>)"
        
        return output
        
    def get_interpreted_data(self, params = None):
        output = {}
        
        if self.current_file:
            interpreted_data = interpret.Interpret.Interpret(self)
            output['disassembly'] = interpreted_data.get_filetype()
            output['version'] = interpreted_data.get_version()
            output['architecture'] = interpreted_data.get_architecture()
            output['compiler'] = interpreted_data.get_compiler()
            output['sections'] = interpreted_data.get_sections()
        else:
            print "No file selected! Please select with",\
                "idamous.set_file(<filename>)"
        
        return output
        
    def get_help(self, params = None):
        print "This is the help menu!"
    
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
    start_shell()
